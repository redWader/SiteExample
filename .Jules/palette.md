## 2026-06-05 - Improve Form UX with Visual Required Indicators and Autocomplete
**Learning:** While the 'required' attribute enforces validation, users need a visual cue (like a red asterisk) *before* submitting to avoid frustration. Also, adding 'autocomplete' helps users fill out standard fields much faster, improving overall accessibility and UX.
**Action:** Always pair HTML5 validation attributes with visual indicators (using aria-hidden so screen readers don't read the asterisk redundantly) and utilize autocomplete for standard user data inputs.
