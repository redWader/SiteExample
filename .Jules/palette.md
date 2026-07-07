## 2024-05-18 - Required Field Indicators Accessibility
**Learning:** Adding visual indicators (like asterisks) to required fields without `aria-hidden="true"` causes redundant screen reader announcements when combined with HTML5 `required` attributes.
**Action:** Always complement HTML5 `required` attributes with explicit visual indicators (e.g., asterisks) that have `aria-hidden="true"` to improve cognitive accessibility without harming screen reader experience.
