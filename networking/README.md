# ProdStack Networking (VPC Simulation)

## Networks
| Network           | Subnet        | Gateway    | Internet | AWS Equivalent      |
|-------------------|---------------|------------|----------|---------------------|
| prodstack-public  | 10.0.1.0/24   | 10.0.1.1   | YES      | Public subnet       |
| prodstack-private | 10.0.2.0/24   | 10.0.2.1   | NO       | Private subnet      |

## DNS Entries (/etc/hosts)
| Local Name                  | Resolves To | AWS Equivalent         |
|-----------------------------|-------------|------------------------|
| prodstack.local             | 127.0.0.1   | Route 53 hosted zone   |
| api.prodstack.local         | 127.0.0.1   | api.internal           |
| db.prodstack.local          | 127.0.0.1   | db.internal            |
| vault.prodstack.local       | 127.0.0.1   | vault.internal         |
| grafana.prodstack.local     | 127.0.0.1   | grafana.internal       |
| prometheus.prodstack.local  | 127.0.0.1   | prometheus.internal    |

## Container Placement Rules
- Load balancer (Nginx) → prodstack-public (+ prodstack-private for upstream)
- App containers (Flask) → prodstack-private only
- Database (Postgres)   → prodstack-private only
- Vault                 → prodstack-private only
- Monitoring            → prodstack-private only
