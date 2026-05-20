class Twitter:

    def __init__(self):
        self.posts = defaultdict(list)
        self.followers = defaultdict(set)
        self.time = 0

    def postTweet(self, userId: int, tweetId: int) -> None:
        self.posts[userId].append([self.time, tweetId])
        self.time -= 1

    def getNewsFeed(self, userId: int) -> List[int]:
        minHeap = []
        res = []
        self.followers[userId].add(userId)
        for i in self.followers[userId]:
            if i in self.posts:
                index = len(self.posts[i]) - 1
                time, Id = self.posts[i][index]
                minHeap.append([time, Id, i, index-1])
        heapq.heapify(minHeap)

        while minHeap and len(res) < 10:
            time, Id, i, ind = heapq.heappop(minHeap)
            res.append(Id)
            if ind >=0:
                time, Id= self.posts[i][ind]
                heapq.heappush(minHeap, [time, Id, i, ind - 1])
        return res



        
        

    def follow(self, followerId: int, followeeId: int) -> None:
        self.followers[followerId].add(followeeId)

    def unfollow(self, followerId: int, followeeId: int) -> None:
        self.followers[followerId].discard(followeeId)
        
        
