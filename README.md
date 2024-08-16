# Python-Cheat-Sheet

# Binary
 
Each 1 in a binary number represents an ever-greater multiple of 2. In a 4-digit number, that means you have the eights place, the fours place, the twos place, and the ones place. Similar to how in decimal you would have the thousands place, the hundreds place, the tens place, and the ones place.

128 - 64 - 32 - 16 - 8 - 4 - 2 - 1

1 --  0  -- 0  -- 1  -- 0  -- 1  -- 0 --  1

128 + 16 + 4 + 1 = 149

Simple as that! Another example: The largest number you can store in 5 digits of binary is 31.


# Bitwise '&' and '|' Operators (AND/OR)

0101 = 5
'&'
0111 = 7
=
0101 = 5

'&' operator requires both to be 1's to be True, so the 01(1)1 is ignored.

0101 = 5
'|'
0111 = 7
=
0111 = 7

'|' operator only requires one of them to be 1's to be True, so the 01(1)1 is not ignored.
