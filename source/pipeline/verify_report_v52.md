# Release verification
folder: `/tmp/claude-0/-home-claude/8d792bb3-ad33-5c0d-9071-132a2ece829d/scratchpad/intaliq`

| route | view | frames (empty) | broken imgs | unresolved use | shot |
|---|---|---|---|---|---|
| home | v-home | 0 (0) | 0 | 0 | home.png |
| unit-01/practice | v-practice | 0 (0) | 0 | 0 | unit-01_practice.png |
| unit-01p/practice | v-practice | 0 (0) | 0 | 0 | unit-01p_practice.png |
| unit-01/student | v-student | 43 (0) | 0 | 0 | unit-01_student.png |
| unit-01/notebook | v-note | 0 (0) | 0 | 0 | unit-01_notebook.png |
| unit-02/notebook | v-note2 | 0 (0) | 0 | 0 | unit-02_notebook.png |
| tour | v-tour | 0 (0) | 0 | 0 | tour.png |
| unit-02/practice | v-practice | 0 (0) | 0 | 0 | unit-02_practice.png |
| unit-02p/practice | v-practice | 0 (0) | 0 | 0 | unit-02p_practice.png |
| unit-02/student | v-student2 | 28 (0) | 0 | 0 | unit-02_student.png |
| unit-03/student | v-student3 | 14 (14) | 0 | 0 | unit-03_student.png |
| unit-03/notebook | v-note3 | 0 (0) | 0 | 0 | unit-03_notebook.png |
| unit-03/practice | v-practice | 0 (0) | 0 | 0 | unit-03_practice.png |
| unit-03p/practice | v-practice | 0 (0) | 0 | 0 | unit-03p_practice.png |

## Digital pathways walked to the end
| unit | pathway | planned tasks | completed | reached end | actions by kind |
|---|---|---:|---:|---|---|
| unit-01 | vocab | 57 | 57 | yes | arabic_to_picture 9, explore 22, listen_tap 9, meaning_in_context 8, picture_to_arabic 9 |
| unit-01 | reading | 31 | 62 | yes | arabic_to_picture 6, either_or 7, explore 14, find_it 3, listen_tap 6, listen_which 3, listen_who 5, meaning_in_context 5, read-done 1, read-more 3, retrieval 2, sequence-check 1, sequence-step 4, true_false 4, who_says 5 |
| unit-01 | reading2 | 15 | 36 | yes | arabic_to_picture 2, either_or 4, explore 6, find_it 1, listen_tap 2, listen_which 3, listen_who 3, meaning_in_context 6, read-done 1, read-more 3, retrieval 1, sequence-check 1, sequence-step 1, true_false 3, who_says 3 |
| unit-02 | vocab | 66 | 66 | yes | arabic_to_picture 22, explore 22, picture_to_arabic 22 |
| unit-02 | reading | 28 | 50 | yes | arabic_to_picture 13, either_or 5, explore 13, find_it 3, read-done 1, read-more 3, retrieval 4, sequence-check 1, sequence-step 5, true_false 6, who_says 4 |
| unit-02 | reading2 | 20 | 39 | yes | arabic_to_picture 9, either_or 4, explore 9, find_it 3, read-done 1, read-more 3, retrieval 3, sequence-check 1, sequence-step 2, true_false 5, who_says 4 |
| unit-03 | vocab | 40 | 40 | yes | arabic_to_picture 2, explore 27, meaning_in_context 9, picture_to_arabic 2 |
| unit-03 | reading | 16 | 54 | yes | arabic_to_picture 1, either_or 5, explore 13, find_it 3, meaning_in_context 16, read-done 1, read-more 3, retrieval 4, sequence-check 1, sequence-step 4, true_false 6, who_says 4 |
| unit-03 | reading2 | 11 | 41 | yes | either_or 4, explore 9, find_it 3, meaning_in_context 12, read-done 1, read-more 3, retrieval 3, sequence-check 1, sequence-step 2, true_false 5, who_says 3 |

## Unit 1 print-task response resources
```
[{"task": "read-match", "pictures": 5, "items": 5}, {"task": "read-match", "pictures": 0, "items": 3}, {"task": "who-says", "faces": 5, "items": 5, "circles": 7}, {"task": "who-says", "faces": 5, "items": 3, "circles": 5}, {"task": "sequence", "items": 4, "boxes": 4}, {"task": "sequence", "items": 3, "boxes": 3}]
```

## Unit 1 language sweep (learner view)
786 Arabic tokens checked on the student and notebook pages; unknown: 0

## Unit 1 task forms
```
{"acts": [{"rubric": true, "items": 4, "english": 0}, {"rubric": true, "items": 5, "english": 0}, {"rubric": true, "items": 4, "english": 0}, {"rubric": true, "items": 5, "english": 0}, {"rubric": true, "items": 5, "english": 0}, {"rubric": true, "items": 4, "english": 0}, {"rubric": true, "items": 3, "english": 0}, {"rubric": true, "items": 3, "english": 0}, {"rubric": true, "items": 3, "english": 0}, {"rubric": true, "items": 3, "english": 0}, {"rubric": true, "items": 2, "english": 0}, {"rubric": true, "items": 4, "english": 0}, {"rubric": true, "items": 3, "english": 0}, {"rubric": true, "items": 6, "english": 0}, {"rubric": true, "items": 4, "english": 0}, {"rubric": true, "items": 4, "english": 0}], "pages": [{"tag": true, "hasNb": true}, {"tag": true, "hasNb": true}, {"tag": true, "hasNb": true}, {"tag": true, "hasNb": true}, {"tag": true, "hasNb": true}, {"tag": true, "hasNb": true}, {"tag": true, "hasNb": true}, {"tag": true, "hasNb": true}], "corner": {"status": "not-delivered", "slots": [false, false, false]}}
```

## Listening machinery (fixture test against the deployed engine)
all listening expectations hold (fixture only — no recording is shipped)

## Mutation tests (deployed engine)
| unit | mutation | delivers | sequence | pathway |
|---|---|---|---:|---:|
| unit-01 | control | YES | 40 | 31 |
| unit-01 | canon_word_added | blocked | 0 | 0 |
| unit-01 | unprinted_form_on_card | blocked | 0 | 0 |
| unit-01 | reading_lists_unknown_id | blocked | 0 | 0 |
| unit-01 | reading_omits_first_sentence | blocked | 0 | 0 |
| unit-01 | audio_flag_without_clips | blocked | 0 | 0 |
| unit-01p | control | YES | 26 | 15 |
| unit-01p | canon_word_added | blocked | 0 | 0 |
| unit-01p | unprinted_form_on_card | blocked | 0 | 0 |
| unit-01p | reading_lists_unknown_id | blocked | 0 | 0 |
| unit-01p | reading_omits_first_sentence | blocked | 0 | 0 |
| unit-01p | audio_flag_without_clips | blocked | 0 | 0 |
| unit-02 | control | YES | 67 | 28 |
| unit-02 | canon_word_added | blocked | 0 | 0 |
| unit-02 | unprinted_form_on_card | blocked | 0 | 0 |
| unit-02 | reading_lists_unknown_id | blocked | 0 | 0 |
| unit-02 | reading_omits_first_sentence | blocked | 0 | 0 |
| unit-02 | audio_flag_without_clips | blocked | 0 | 0 |
| unit-02p | control | YES | 49 | 20 |
| unit-02p | canon_word_added | blocked | 0 | 0 |
| unit-02p | unprinted_form_on_card | blocked | 0 | 0 |
| unit-02p | reading_lists_unknown_id | blocked | 0 | 0 |
| unit-02p | reading_omits_first_sentence | blocked | 0 | 0 |
| unit-02p | audio_flag_without_clips | blocked | 0 | 0 |
| unit-03 | control | YES | 34 | 16 |
| unit-03 | canon_word_added | blocked | 0 | 0 |
| unit-03 | unprinted_form_on_card | blocked | 0 | 0 |
| unit-03 | reading_lists_unknown_id | blocked | 0 | 0 |
| unit-03 | reading_omits_first_sentence | blocked | 0 | 0 |
| unit-03 | audio_flag_without_clips | blocked | 0 | 0 |
| unit-03p | control | YES | 31 | 11 |
| unit-03p | canon_word_added | blocked | 0 | 0 |
| unit-03p | unprinted_form_on_card | blocked | 0 | 0 |
| unit-03p | reading_lists_unknown_id | blocked | 0 | 0 |
| unit-03p | reading_omits_first_sentence | blocked | 0 | 0 |
| unit-03p | audio_flag_without_clips | blocked | 0 | 0 |

## Blockers
- none

## Warnings
- Unit 1 authentic corner: NOT DELIVERED — 0 of 3 photographs present (Batch 2; the unit is not complete)
- art files used more than once (check each is a legitimate reuse): assets/art/unit1-rich/u1-face-huda.png, assets/art/unit1-rich/u1-face-karim.png, assets/art/unit1-rich/u1-face-sara.png, assets/art/unit1-rich/u1-s1-1.png, assets/art/unit1-rich/u1-s1-2.png, assets/art/unit1-rich/u1-s1-3.png, assets/art/unit1-rich/u1-s1-4.png, assets/art/unit1-rich/u1-s1-5.png, assets/art/unit1-rich/u1-s1-6.png, assets/art/unit1-rich/u1-s2-1.png, assets/art/unit1-rich/u1-s2-2.png, assets/art/unit1-rich/u1-s2-3.png, assets/art/unit1-rich/u1-support-list.png, assets/art/unit2-rich/av-omar.png, assets/art/unit2-rich/av-rana.png, assets/art/unit2-rich/av-razan.png, assets/art/unit2-rich/u2-s1-1.png, assets/art/unit2-rich/u2-s1-2.png, assets/art/unit2-rich/u2-s1-3-v43.png, assets/art/unit2-rich/u2-s1-4.png, assets/art/unit2-rich/u2-s1-5-v43.png, assets/art/unit2-rich/u2-s1-6.png, assets/art/unit2-rich/u2-s1-7.png, assets/art/unit2-rich/u2-s1-8.png, assets/art/unit2-rich/u2-s2-1.png, assets/art/unit2-rich/u2-s2-2.png, assets/art/unit2-rich/u2-s2-3.png, assets/art/unit2-rich/u2-s2-4-v43.png, assets/art/unit2-rich/u2-s2-5.png, assets/art/unit2-rich/u2-s2-6.png
- "illustration pending" appears 1× — confirm each is intended
- "PROPOSED" appears 2× — confirm each is intended
- external resource not reachable from this workspace (fine on Pages): https://fonts.googleapis.com/css2?family=Baloo+Bhaijaan+2:wght@500;700;800&family=Noto+Nas