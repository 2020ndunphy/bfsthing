def path_finder(maze):
   matrix = list(map(list, a.splitlines()))
   length = len(matrix)
   s = (0,0)
   t = (length - 1,length - 1)
   level = {s: 0}
   parent = {s: 0}
   i = 1
   frontier = [s]
   #setting up starting point in maze
   while frontier:
       next = []
       #moving to next level in maze
       for u in frontier:
           x,y = u
           for u in Adj[u]:
               if u not in level:
               #if point hasn't been found yet
                   level[u] = i
                   parent[u] = u
                   next.append(u)
                   #continuing to find point
       frontier = next
       i+=1
       #looping to find point

   return next
   #return when found
