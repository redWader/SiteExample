## 2024-06-01 - Visual Required Indicators

**Learning:** When a form field uses the HTML `required` attribute, screen readers will already announce that the field is required. Adding a visual indicator like an asterisk (`*`) is helpful for sighted users, but to prevent screen readers from reading it aloud redundantly (or reading "star"), it's best practice to hide the visual indicator from screen readers using `aria-hidden="true"`. Placeholders also provide extra contextual help and clarity for users.

**Action:** Always add visual indicators for required fields to support sighted users. Pair visual indicators with `aria-hidden="true"` when the input element already has a programmatic `required` attribute. Include descriptive placeholders for clearer form instructions.