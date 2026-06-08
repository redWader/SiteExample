## 2024-03-24 - Screen Reader Context & Form Clarity
**Learning:** Found an accessibility pattern where "Read more" (Подробнее) links lacked context for screen readers, and required form fields lacked visual indicators. In Russian localization, default Bootstrap ARIA labels (like "Toggle navigation") were also left in English.
**Action:** Always add descriptive `aria-label`s to generic links (e.g., `aria-label="Подробнее о проекте E-commerce Платформа"`), add visual `*` indicators to required form fields, and localize ARIA attributes when working with non-English interfaces.
