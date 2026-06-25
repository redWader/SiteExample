## 2024-06-25 - Explicit Required Field Indicators
**Learning:** While HTML5 `required` attributes handle browser validation, they do not provide clear visual cues for cognitive accessibility. Users shouldn't have to submit a form to find out what's required.
**Action:** Added explicit red asterisks (`<span class="text-danger" aria-hidden="true">*</span>`) to required form fields. The `aria-hidden="true"` prevents redundant screen reader announcements, since the input itself already has the `required` attribute.
