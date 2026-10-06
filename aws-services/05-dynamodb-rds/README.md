# DynamoDB and RDS - Database Services

**Name:** Raghavendra  
**Enrollment number:** 24BCS10250

**Session:** 18

## DynamoDB

DynamoDB is a managed NoSQL database. A table contains items, and each item contains attributes. Items do not need the same set of non-key attributes.

The partition key determines how data is distributed. A simple primary key uses only a partition key. A composite primary key uses a partition key and sort key. Items sharing a partition key are distinguished and ordered by the sort key. Key design should follow the queries the application needs.

For example, a notes table could use `student_id` as its partition key and `note_id` as its sort key. Fetching one student's notes matches that access pattern. A design that concentrates all traffic on one partition key can become a hotspot.

Common uses are session data, key-value lookups, shopping carts and applications needing predictable low-latency access. It does not provide the same join model as a relational SQL database.

## RDS

RDS manages relational database instances. Supported database families include MySQL, MariaDB, PostgreSQL, Oracle, SQL Server and Db2. Amazon Aurora provides MySQL- and PostgreSQL-compatible engines.

A DB instance has an engine, compute capacity and storage. Tables have relational structure, and applications use SQL. Security includes private networking, security groups, authentication and encryption. Database passwords should not be committed to Git.

Automated backups support point-in-time recovery within the configured retention period. Manual snapshots are retained until deleted. Multi-AZ options provide availability and failover; their exact readable-replica behavior depends on the deployment type. Read replicas serve read traffic and have different replication and failover purposes.

For a small relational notes app, RDS PostgreSQL could store students and notes with foreign keys. Common uses include transactional applications, reporting and existing software that expects SQL.

| DynamoDB | RDS |
|---|---|
| NoSQL items and attributes | Relational tables and SQL |
| Key and query pattern design is central | Schema and relationships are central |
| Managed scaling options | Instance and engine capacity choices |
| Suitable for key-value access | Suitable for relational queries and transactions |

[DynamoDB basics](https://docs.aws.amazon.com/amazondynamodb/latest/developerguide/HowItWorks.html), [RDS overview](https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/Welcome.html).
