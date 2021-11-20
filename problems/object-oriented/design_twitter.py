""" 
Design Twitter

Reference: https://leetcode.com/problems/design-twitter/

Design a simplified version of Twitter where users can post tweets,
follow/unfollow another user, and is able to see the 10 most recent tweets in
the user's news feed.   

Implement the Twitter class:

Twitter() Initializes your twitter object.

postTweet(int userId, int tweetId): Composes a new tweet with ID tweetId by
the user userId. Each call to this function will be made with a unique tweetId.

getNewsFeed(int userId): Retrieves the 10 most recent tweet IDs in
the user's news feed. Each item in the news feed must be posted by users who
the user followed or by the user themself. Tweets must be ordered from most
recent to least recent. 

follow(int followerId, int followeeId): The user with ID followerId started
following the user with ID followeeId.  

unfollow(int followerId, int followeeId): The user with ID followerId
started unfollowing the user with ID followeeId. 

Example 1:

Input
["Twitter", "postTweet", "getNewsFeed", "follow", "postTweet", "getNewsFeed", "unfollow", "getNewsFeed"]
[[], [1, 5], [1], [1, 2], [2, 6], [1], [1, 2], [1]]
Output
[null, null, [5], null, null, [6, 5], null, [5]]

Explanation
Twitter twitter = new Twitter();
twitter.postTweet(1, 5); // User 1 posts a new tweet (id = 5).
twitter.getNewsFeed(1);  // User 1's news feed should return a list with 1 tweet id -> [5]. return [5]
twitter.follow(1, 2);    // User 1 follows user 2.
twitter.postTweet(2, 6); // User 2 posts a new tweet (id = 6).
twitter.getNewsFeed(1);  // User 1's news feed should return a list with 2 tweet ids -> [6, 5]. Tweet id 6 should precede tweet id 5 because it is posted after tweet id 5.
twitter.unfollow(1, 2);  // User 1 unfollows user 2.
twitter.getNewsFeed(1);  // User 1's news feed should return a list with 1
tweet id -> [5], since user 1 is no longer following user 2.
"""


class User:
    def __init__(self, userId):
        self.userID = userId
        self.follows = set()


class Twitter:
    def __init__(self):
        self.users = {}
        self.tweets = []
        self.max_tweets = 10

    def createUser(self, userId):
        if userId not in self.users:
            self.users[userId] = User(userId)

    def postTweet(self, userId, tweetId):
        """
        :type userId: int
        :type tweetId: int
        :rtype: None
        """
        if not isinstance(userId, int) or not isinstance(tweetId, int):
            raise ValueError("Invalid post!")
        self.createUser(userId)
        self.tweets.append((userId, tweetId))

    def getNewsFeed(self, userId):
        """
        :type userId: int
        :rtype: List[int]
        """
        right_pointer = len(self.tweets) - 1
        counter, feed = 0, []

        while right_pointer >= 0 and counter <= self.max_tweets:
            # if userID is in the latest tweet, add to feed
            # or if userID of tweet is in the follow list of userID
            if (
                self.tweets[right_pointer][0] == userId
                or self.tweets[right_pointer][0] in self.users[userId].follows
            ):
                feed.append(self.tweets[right_pointer][1])
                counter += 1
            right_pointer -= 1
        return feed

    def follow(self, followerId, followeeId):
        """
        :type followerId: int
        :type followeeId: int
        :rtype: None
        """
        self.createUser(followerId)
        self.createUser(followeeId)
        self.users[followerId].follows.add(followeeId)

    def unfollow(self, followerId, followeeId):
        """
        :type followerId: int
        :type followeeId: int
        :rtype: None
        """
        self.createUser(followerId)
        self.createUser(followeeId)
        if followeeId in self.users[followerId].follows:
            self.users[followerId].follows.remove(followeeId)


if __name__ == "__main__":
    t = Twitter()
    print("post tweet:", t.postTweet(1, 5))
    print("get newsfeed:", t.getNewsFeed(1))
    print("following:", t.follow(1, 2))
    print("post tweet:", t.postTweet(2, 6))
    print("get newsfeed:", t.getNewsFeed(1))
    print("unfollow:", t.unfollow(1, 2))
    print("get newsfeed", t.getNewsFeed(1))
