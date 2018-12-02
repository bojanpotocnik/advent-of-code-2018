# noinspection SpellCheckingInspection
"""
--- Day 2: Inventory Management System ---

-- Part One --

You stop falling through time, catch your breath, and check the screen on the device. "Destination reached. Current
Year: 1518. Current Location: North Pole Utility Closet 83N10." You made it! Now, to find those anomalies.

Outside the utility closet, you hear footsteps and a voice. "...I'm not sure either. But now that so many people have
chimneys, maybe he could sneak in that way?" Another voice responds, "Actually, we've been working on a new kind of
suit that would let him fit through tight spaces like that. But, I heard that a few days ago, they lost the prototype
fabric, the design plans, everything! Nobody on the team can even seem to remember important details of the project!"

"Wouldn't they have had enough fabric to fill several boxes in the warehouse? They'd be stored together, so the box IDs
should be similar. Too bad it would take forever to search the warehouse for two similar box IDs..." They walk too far
away to hear any more.

Late at night, you sneak to the warehouse - who knows what kinds of paradoxes you could cause if you were
discovered - and use your fancy wrist device to quickly scan every box and produce a list of the likely candidates
(your puzzle input).

To make sure you didn't miss any, you scan the likely candidate boxes again, counting the number that have an ID
containing exactly two of any letter and then separately counting those with exactly three of any letter. You can
multiply those two counts together to get a rudimentary checksum and compare it to what your device predicts.

For example, if you see the following box IDs:

    - `abcdef` contains no letters that appear exactly two or three times.
    - `bababc` contains two `a` and three `b`, so it counts for both.
    - `abbcde` contains two `b`, but no letter appears exactly three times.
    - `abcccd` contains three `c`, but no letter appears exactly two times.
    - `aabcdd` contains two `a` and two `d`, but it only counts once.
    - `abcdee` contains two `e`.
    - `ababab` contains three `a` and three `b`, but it only counts once.

Of these box IDs, four of them contain a letter which appears exactly twice, and three of them contain a letter which
appears exactly three times. Multiplying these together produces a checksum of `4 * 3 = 12`.

What is the checksum for your list of box IDs?

To begin, `get your puzzle input. <https://adventofcode.com/2018/day/2/input>`_ >> `input.txt`


-- Part Two --

Confident that your list of box IDs is complete, you're ready to find the boxes full of prototype fabric.

The boxes will have IDs which differ by exactly one character at the same position in both strings.
For example, given the following box IDs:

    - `abcde`
    - `fghij`
    - `klmno`
    - `pqrst`
    - `fguij`
    - `axcye`
    - `wvxyz`

The IDs abcde and axcye are close, but they differ by two characters (the second and fourth). However, the IDs `fghij`
and `fguij` differ by exactly one character, the third (`h` and `u`). Those must be the correct boxes.

What letters are common between the two correct box IDs? (In the example above, this is found by removing the differing
character from either ID, producing `fgij`.)
"""

import timing

# The collections.Counter class could be used, however its advanced features are not required here
# and only decrease the performance (it takes almost three times as long as the current solution).

with open("input.txt") as f:
    ids = [line.strip() for line in f]

# region Part One
counter_two: int = 0
counter_three: int = 0

for code in ids:
    char_counts = dict.fromkeys(code, 0)
    # Count all of the chars first because of "... containing *exactly* two/three of any letter ..."
    for c in code:
        char_counts[c] += 1
    # Check if there are any chars occurring exactly two or three times, but count each only once!
    # Two for-loops are faster (tested) than using booleans in single for loop.
    for c_count in char_counts.values():
        if c_count == 2:
            counter_two += 1
            break
    for c_count in char_counts.values():
        if c_count == 3:
            counter_three += 1

result = counter_two * counter_three

print(f"Part 1 - Answer: {counter_two} * {counter_three} = [{result}] (took {timing.time_string()})")
# endregion Part One

# region Part Two
timing.reset()

common_chars: str = None

for code_i, code in enumerate(ids):
    for other_code in ids[code_i:]:  # All of the previous codes were once already compared.
        # Save the indices of all chars which differs from the other code.
        diffs = [i for i, c in enumerate(code) if (c != other_code[i])]
        # The boxes will have IDs which differ by exactly one character at the same position in both strings.
        if len(diffs) == 1:
            common_chars = code[:diffs[0]] + code[diffs[0] + 1:]  # Take all of the chars except the different one.
            # There are only two such boxes.
            break

print(f"Part 2 - Answer: [{common_chars}] (took {timing.time_string()})")

# endregion Part Two
