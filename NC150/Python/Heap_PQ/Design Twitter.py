# Time: O(10*logk)
class Twitter:

    def __init__(self):
        self.count = 0
        self.followMap = defaultdict(set)
        self.tweetMap = defaultdict(list)
        

    def postTweet(self, userId: int, tweetId: int) -> None:
        self.tweetMap[userId].append([self.count, tweetId])
        self.count -=1
        

    def getNewsFeed(self, userId: int) -> List[int]:
        res = []
        maxHeap = []
        self.followMap[userId].add(userId)
        for followeeId in self.followMap[userId]:
            if(self.tweetMap[followeeId]):
                index = len(self.tweetMap[followeeId]) - 1
                count, tweetId = self.tweetMap[followeeId][index]
                maxHeap.append([count, followeeId, tweetId, index-1])
        heapq.heapify(maxHeap)
        k = 10
        while(maxHeap and k > 0):
            count, followeeId, tweetId, index = heapq.heappop(maxHeap)
            print(tweetId)
            res.append(tweetId)
            if(index >= 0):
                count, tweetId = self.tweetMap[followeeId][index]
                heapq.heappush(maxHeap,[count,followeeId, tweetId, index-1])
            k-=1
        return res
        
    def follow(self, followerId: int, followeeId: int) -> None:
        self.followMap[followerId].add(followeeId)

    def unfollow(self, followerId: int, followeeId: int) -> None:
        if(followeeId in self.followMap[followerId]):
            self.followMap[followerId].remove(followeeId)


# Your Twitter object will be instantiated and called as such:
# obj = Twitter()
# obj.postTweet(userId,tweetId)
# param_2 = obj.getNewsFeed(userId)
# obj.follow(followerId,followeeId)
# obj.unfollow(followerId,followeeId)