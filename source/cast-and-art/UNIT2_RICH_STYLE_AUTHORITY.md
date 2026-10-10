# Unit 2 Rich-Cartoon Authority

SC-113 records the owner's direct style choice in this chat. The reference is the shared Four Friends and the Golden Keys artwork, not sparse Execution A. Reference PNGs and their SHA-256 hashes are preserved under `references/rich-cartoon/`.

Scope is Unit 2 only. Unit 1 remains its existing pre-calibration art; Unit 3 art is not part of this change. This is a deliberate unit-scoped rendering exception, not a claim that the whole course already has one uniform style.

Full colour, shaded faces, dimensional clothing and props, and backgrounds matching the reference are permitted. No new narrative event, spoiler or extra person is permitted by that stylistic freedom. Icons and portraits have white backgrounds. Generic action figures have no faces. No in-image text or romance-readable pairings.

## Identities

| Character | Fixed Marker | Clothing |
|---|---|---|
| Karim | Crown curls | Blue top, tan trousers |
| Zayd | Grey flat cap | Green top, grey trousers |
| Maha | High topknot | Coral top, blue trousers |
| Omar | Straight upward spikes, never curls | Green top, grey trousers |
| Razan | Exactly two low side bundles | Teal top, navy trousers |
| Khadija | Two long front plaits | Coral top, navy trousers |
| Rana | Chin-length bob | Mustard top, blue trousers |
| Cat | Orange-white, triangular ears, curled tail | Not applicable |

Karim's large satchel is brown. Zayd's existing small satchel in Story 1 frame 4 is black. SC-116 changes the generic learner-facing small `obj-bag` icon to brown at the owner's request, matching the dominant narrative bag colour; the story frame is unchanged. The two object slots still distinguish small and large bags, not colour. Photo figures retain Razan's bundles and Khadija's plaits and are faceless inside the small prints.

## Preservation And Acceptance

High-resolution raw generated PNGs are retained unchanged; CSS fits them without cropping. Corrections become new versioned files. Superseded PNGs remain byte-exact and their hashes remain in the production manifest. Style approval does not waive per-image content review at strip size.

Version A must differ only in its specified book/key and cat/book areas; every other pixel must match the appropriate Story 1 source. A fresh scene generation cannot pass that requirement merely by looking similar.

SC-115 records the owner's explicit Version A-only targeted compositing exception. Generated book artwork is inserted and original cat pixels re-layered without moving them. The final derived PNGs are accepted production assets; integration uses their exact bytes. Source hashes, change rectangles, and the generated insertion hash are in the manifest; `derive_version_a.py` makes this reproducible. The focused gate proves outside-region identity.
