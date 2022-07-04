### SQL 분류

- **DDL : Data Definition Language**  
데이터 정의어란? 데이터베이스를 정의하는 언어이며, 데이터를 생성, 수정, 삭제하는 등의 데이터의 전체의 골격을 결정하는 역할을 하는 언어
    - CREATE
    - ALTER
    - DROP
    - RENAME
    - TRUNCATE

- **DML : Data Manipulation Language**  
데이터 조작어란? 정의된 데이터베이스에 입력된 레코드를 조회하거나 수정하거나 삭제하는 등의 역할을 하는 언어
    - SELECT
    - INSERT
    - UPDATE
    - DELETE

- **DCL : Data Control Language**  
    - GRANT
    - REVOKE

- **TCL : Transaction Control Language**  
    - COMMIT
    - ROLLBACK
    - SAVEPOINT

### ERD (Entity Relationship Diagram) Conceptual Model  

- DBMS를 기능에 맞게 디자인 하는 것
- Entity = Table
- Entity Set : Entity를 정의하고 있는 집합으로 속성(attribute)을 정의함
    - Primary Key (PK)       
- Relationship : Entity 사이의 관계, 주로 어떤 “기능”을 나타냄
- Relationship Set : entity들 사이의 모든 relationship을 모은 집합
    - with attributes
- Ternary Relationship
- Relationship with complex attributes
- Mapping Cardinalities : ERD에서 table과 table 사이의 관계를 정의 (생기는 것이 아니라 만드는 것)
    - One-to-One
    - One-to-Many : 하나의 객체가 다수의 객체를 매핑하는 것
    - Many-to-One
    - Many-to-Many
- Reduction ERD to Schema  
  **Conceptual Model(ERD) → Logical Model(Schema)**
