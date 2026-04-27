class Twitter:

    class Tweet():

        def __init__(self, tweetId, order):
            self.tweetId = tweetId
            self.order = -order
        
        def __lt__(self, other):
            return self.order < other.order

    class User:
        def __init__(self, userId):
            self.userId = userId
            self.following = {}
            self.tweets = []

        def post(self, tweet):
            self.tweets.append(tweet)
        
        def getNewsFeed(self):

            feed = []
            # print("getfeed called")
            for other in self.following.values():
                # print(f"checking to see if {other.userId} has any tweets")
                for tweet in other.tweets:
                    # print(f"tweet id: {tweet}")
                    heapq.heappush(feed, tweet)

            for tweet in self.tweets:
                heapq.heappush(feed, tweet)
                
            k = 0
            ans = []
            while k < 10 and feed:
                k+= 1
                ans.append(heapq.heappop(feed).tweetId)

            return ans


        def subscribe(self, other):
            # print(f"{self.userId} subscribed to {other.userId}")
            if self.userId == other.userId:
                return
            self.following[other.userId] = other

        
        def unsubscribe(self, other):
            # print(f"{self.userId} trying unsubscribe to {other.userId}")

            if other.userId not in self.following:
                return
            # print(f"{self.userId} unsubscribed to {other.userId}")

            self.following.pop(other.userId)
            
        
    def __init__(self):
        # self.tweets = []
        self.users = {}
        self.order = 0

    def postTweet(self, userId: int, tweetId: int) -> None:
        # print("tweeting ", userId, " ", tweetId)
        if userId not in self.users:
            self.users[userId] = self.User(userId)

        tweet = self.Tweet(tweetId, self.order)
        self.order+= 1
        self.users[userId].post(tweet)

    def getNewsFeed(self, userId: int) -> List[int]:
        if userId not in self.users:
            return []
        return self.users[userId].getNewsFeed()
        

    def follow(self, followerId: int, followeeId: int) -> None:
        if followerId not in self.users:
            self.users[followerId] = self.User(followerId)

        if followeeId not in self.users:
            self.users[followeeId] = self.User(followeeId)


        self.users[followerId].subscribe(self.users[followeeId])
        

    def unfollow(self, followerId: int, followeeId: int) -> None:
        if followerId not in self.users or followeeId not in self.users:
            # print("fked")
            return 

        self.users[followerId].unsubscribe(self.users[followeeId])

        
