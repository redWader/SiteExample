## 2026-07-01 - Required Form Fields Accessibility
**Learning:** Using HTML5 `required` attribute is good, but without explicit visual indicators (like asterisks), cognitive accessibility suffers as users aren't visually prompted about required fields before submission. Adding `aria-hidden="true"` to visual indicators prevents redundant screen reader announcements while helping sighted users.
**Action:** Always complement HTML5 `required` attributes with visual indicators containing `aria-hidden="true"` to improve cognitive accessibility without harming screen reader experience.
