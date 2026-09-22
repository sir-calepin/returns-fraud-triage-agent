# Happy-Path Evaluation Scenarios

## HP-01 — Standard in-window return

**Input:** Return request for order `#4821`; delivered six days ago; unopened item; order and customer match.

**Expected behavior:** Route as routine / low risk.

**Pass criterion:** The output identifies the order match and in-policy timing, does not add a fraud flag, and does not make a final refund decision.

## HP-02 — Damaged item with evidence

**Input:** Order `#5531`; customer reports damage and provides photo reference and serial number.

**Expected behavior:** Route to normal review with damage noted.

**Pass criterion:** The output identifies this as a fulfillment or condition issue, not a fraud finding.

## HP-03 — Standard size mismatch

**Input:** Order `#6120`; customer requests return because size does not fit; request is in the policy window.

**Expected behavior:** Route normally.

**Pass criterion:** The output identifies routine return handling and no repeat-return risk.

## HP-04 — Wrong item shipped

**Input:** Order `#1177`; customer reports receiving a different item than ordered.

**Expected behavior:** Route to fulfillment review, not fraud review.

**Pass criterion:** The output distinguishes a fulfillment issue from suspicious behavior.

## HP-05 — First return from account

**Input:** Order `#1044`; customer has no recent returns; request is within policy and serial matches.

**Expected behavior:** Route normally.

**Pass criterion:** No repeat-return flag, no unnecessary escalation.
