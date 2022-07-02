n, a, b = list(map(int, input().split()))
minutes = list(map(int, input().split()))

for i in range(len(minutes)):
    if minutes[i] > 45 + a:
            if minutes[i] > minutes[i + 1]:
                print("NO")
                break
    elif minutes[i] > 90 + b:
        print("NO")
        break

    
            
    
    
    
    
    

    

