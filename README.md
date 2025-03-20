```mermaid
graph TD
    subgraph System
        style System fill:#ffffff,stroke:#000000,stroke-width:2px

        User([Пользователь [Person]])
        FE[Микросервис Frontend [Component]]
        BE[Микросервис Backend [Django REST framework]]
        DB[База данных [Container: SQLite]]
        Test[Микросервис тестирования [Playwright, Locus]]

        User --> FE
        FE -->|API| BE
        BE --> DB
        Test --> DB
        Test --> BE
    end

    style User fill:#003366,color:#ffffff
    style FE fill:#4169e1,color:#ffffff
    style BE fill:#4169e1,color:#ffffff
    style DB fill:#4169e1,color:#ffffff
    style Test fill:#4169e1,color:#ffffff

    note bottom of System
        Микросервисная система отслеживания данных о согласовании заявок на проведение ремонтных работ
    end