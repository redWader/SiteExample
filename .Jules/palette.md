## 2024-03-24 - Visual Indicators for Required Fields
**Learning:** While the HTML5 `required` attribute provides validation, relying on it alone without explicit visual indicators (like an asterisk) reduces cognitive accessibility, especially for users who might not realize a field is mandatory until they attempt to submit.
**Action:** Always complement the `required` attribute with explicit visual cues (e.g., `<span class="text-danger" aria-hidden="true">*</span>`) in the form labels to improve cognitive accessibility and user expectations.
