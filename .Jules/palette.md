## 2024-06-02 - Visual Indicators for Required Form Fields
**Learning:** Users can be confused when required form fields lack visual indicators, even if the HTML `required` attribute is present, as sighted users cannot easily see `required` attributes without visual cues.
**Action:** Always include a visual indicator like a red asterisk (`<span class="text-danger" aria-hidden="true">*</span>`) on labels for inputs marked as `required`.
