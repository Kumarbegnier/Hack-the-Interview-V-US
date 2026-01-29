def receivedText(S):
    sys.setrecursionlimit(10**7)
    n = len(S)

    def solve(i, left, right, num_lock):
        # stop when all characters are processed
        if i == n:
            return left, right

        ch = S[i]

        if ch == '<':                  # Home
            while left:
                right.append(left.pop())

        elif ch == '>':                # End
            while right:
                left.append(right.pop())

        elif ch == '*':                # Backspace
            if left:
                left.pop()

        elif ch == '#':                # Num Lock toggle
            num_lock = not num_lock

        else:                           # Normal character
            if ch.isdigit() and not num_lock:
                pass                   # ignore digit
            else:
                left.append(ch)

        return solve(i + 1, left, right, num_lock)

    left, right = solve(0, [], [], True)
    return ''.join(left) + ''.join(reversed(right))
