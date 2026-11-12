# Municipal IT Deployment & Operations Runbook

> **Target Environment:** City of Skopje / PE "Parks and Greenery" Local Server Infrastructure  
> **System:** Project VERDANT City Enclave  
> **Security Profile:** Offline-capable, on-premise, zero external network egress  

---

## 1. System Requirements

- **Operating System:** Ubuntu 22.04 LTS / Debian 12 (or Red Hat Enterprise Linux 9).
- **Hardware:**
  - CPU: 8+ cores (x86_64, e.g. Intel Xeon / AMD EPYC).
  - RAM: 32 GB minimum (64 GB recommended for multi-user review sessions).
  - GPU: Optional but recommended (NVIDIA RTX 3080/4080 with 16GB+ VRAM; CPU fallback fully supported).
  - Storage: 1 TB NVMe SSD (RAID 1 mirrored recommended for archival scans).
- **Prerequisites:** Docker Engine 24.0+, Docker Compose v2, OpenSSL.

---

## 2. Quickstart Installation (Offline Bundle)

```bash
# 1. Transfer the deployment tarball to the offline enclave server
tar -xvf verdant-enclave-v2.0.tar.gz
cd verdant-enclave/

# 2. Verify image integrity and environment secrets
cp .env.example .env
chmod 600 .env
# Edit .env with local database passwords and secure session secrets

# 3. Launch the container stack
docker compose -f docker-compose.prod.yml up -d

# 4. Verify local container health
docker compose ps
curl -k http://localhost:8080/health
```

---

## 3. Backup and Disaster Recovery

### Automated Nightly Database Backup
A daily cron job dumps the PostgreSQL/PostGIS database and encrypts the backup:
```bash
#!/bin/bash
BACKUP_DIR="/var/backups/verdant"
DATE=$(date +%Y%m%d_%H%M%S)
mkdir -p "$BACKUP_DIR"

docker exec -t verdant_db pg_dump -U verdant_admin -F c verdant_cadastre > "$BACKUP_DIR/db_$DATE.dump"
# Retain last 30 daily backups
find "$BACKUP_DIR" -type f -name "db_*.dump" -mtime +30 -delete
```

### Complete System Restore
```bash
# Stop backend services
docker compose stop api review_ui

# Restore database from archive dump
docker exec -i verdant_db pg_restore -U verdant_admin -d verdant_cadastre --clean "$BACKUP_DIR/db_20261112.dump"

# Restart stack
docker compose start
```

---

## 4. Rollback Procedure

If a software update requires rollback:
```bash
# Pull previous container tag
docker compose -f docker-compose.prod.yml down
docker tag verdant-api:v2.0.1 verdant-api:rollback
docker compose -f docker-compose.v2.0.0.yml up -d
```
All raw permit files are stored in an append-only, immutable directory (`/var/data/raw_permits/`), ensuring that software rollbacks never affect original scanned documents.
