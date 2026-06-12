## 2024-05-18 - Контекст для ссылок "Подробнее"
**Learning:** Generic link texts like "Подробнее" (Read more) lack context for screen reader users, making it difficult for them to understand where the link leads if read out of context of the surrounding content (like a project card).
**Action:** Always add descriptive `aria-label`s localized to the application's language (e.g., `aria-label="Подробнее о проекте E-commerce Платформа"`) to generic links to provide complete context for assistive technologies.
