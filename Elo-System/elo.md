Player1 : 1200 = R(1)
Player2: 1100 = R(2)

Transformed Ratings:
R(1)' = 10 ^ (R(1) / 400) = 1000
R(2)' = 10 ^ (R(2) / 400) = 562.3413

Expected score ( E ):
E(1) = R(1)' / (R(1)' + R(2)') = 0.6400649998
E(2) = R(2)' / (R(1)' + R(2)') = 1088.48207999

Result ( S ) - 1 for win, 0 for lose

Updated Elo rating ( K = K-factor, being 32 )
r''(1) = r(1) + K * ( S(1) - E(1)) = 1211.51792001
r''(2) = r(2) + K * ( S(2) - E(2)) = 1088.48207999
-> in case player 1 won