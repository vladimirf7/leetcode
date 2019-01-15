"""solved, easy"""

class Solution:
    def numUniqueEmails(self, emails):
        """
        :type emails: List[str]
        :rtype: int
        """
        unique = set()

        for email in emails:
            index = email.find("@")
            unique.add(
                email[:index].split("+")[0].replace(".", "") + email[index:])
        
        return len(unique)
        

if __name__ == "__main__":
    assert Solution().numUniqueEmails([
        "test.email+alex@leetcode.com",
        "test.e.mail+bob.cathy@leetcode.com",
        "testemail+david@lee.tcode.com"]
    ) == 2