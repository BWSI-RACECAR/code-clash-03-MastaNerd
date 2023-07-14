class Solution:    
    def propcontrol(self, center, res):
             if center < res[0] and center < res[1]:
                 return 0
            oneValue = (res[0] + res[1])/2
            turn = (center - oneValue)/oneValue
            return turn
            
            #TODO: Write code below to return a float with the solution to the prompt.
            pass
        
        

def main():
    center = int(input().strip())
    resx = int(input().strip())
    resy = int(input().strip())
    res = (resx, resy)

    tc1 = Solution()
    ans = tc1.propcontrol(center, res)
    ans=format(ans, ".6f")
    print(ans)

if __name__ and "__main__":
    main()
