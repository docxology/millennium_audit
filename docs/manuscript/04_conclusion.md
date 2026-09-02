# Conclusion

The MillenniumLean package is kernel-honest and mathematically empty with
respect to its headline claim. Its build receipt is real - we reproduce it
byte-for-byte - and irrelevant: the types the kernel certifies are
tautologies, substitutions, list identities, faithful definitions of open
problems, and implications whose premises are the prizes themselves.

Three lessons generalize beyond this package.

1. **Axiom footprints audit trust, not content.** `#print axioms` catches
   `sorryAx` and project axioms; it cannot see unproved premises, which live
   in binder types. Any "0 axioms" receipt must be paired with a
   statement-level audit of what the theorems say.
2. **Positive controls need failure modes.** A control that certifies
   `0 < n + 1` alongside "Perelman's theorem" tests nothing.
3. **Defining an open problem in a proof assistant is zero evidence.** The
   kernel will happily check the definition forever.

The six remaining Clay Millennium Problems remain open. The honest
formalization community says so; so does every type in this package, read
closely.
