```mermaid
C4Context
title Микросервисная система отслеживания данных о согласовании заявок на проведение ремонтных работ

Person(User, "Пользователь", "[Person]")

Boundary(b1, "") {
  System(FE, "Микросервис Frontend", "[Component]")
  System(BE, "Микросервис Backend", "[Django REST framework]")
  SystemDb(DB, "База данных", "Container: [SQLite]")
  System(TESTS, "Микросервис тестирования", "[Playwright, Locust]")
}

Rel(User, FE, "")
BiRel(FE, BE, "API")
Rel(BE, DB, "API")
Rel(TESTS, DB, "API")
