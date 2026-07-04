## 2024-05-15 - Form Accessibility & ARIA Localization
**Learning:** HTML5 `required` attributes alone are insufficient for cognitive accessibility. Users need explicit visual indicators. Additionally, ARIA attributes like `aria-label` must match the primary language of the application (Russian in this case) for screen readers to properly announce them.
**Action:** Always complement `required` attributes with visual cues (e.g., asterisks with `aria-hidden="true"`) and explicitly localize any framework-provided ARIA labels to the app's language.
