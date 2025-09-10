class Solution(object):
    def restoreIpAddresses(self, s):

        result = []
        path = []

        def run(idx):

            if len(path)==4 and idx==len(s):
                result.append(".".join(path[:]))
                return

            if len(path) >= 4:
                return

            for i in range(idx, min(idx+3, len(s))):
                subs = s[idx:i+1]

                if len(subs) > 1 and subs[0] == "0":
                    break

                if 0 <= int(subs) <= 255:
                    path.append(subs)
                    run(i+1)
                    path.pop()

        run(0)
        return result