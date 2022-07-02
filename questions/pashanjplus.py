blog_posts = [{'Photos': 3, 'Likes': 21, 'Comments': 2}, {'Likes': 13, 'Comments': 2, 'Shares': 1}, {'Photos': 5, 'Likes': 33, 'Comments': 8, 'Shares': 3}, {'Comments': 4, 'Shares': 2}, {'Photos': 8, 'Comments': 1, 'Shares': 1}, {'Photos': 3, 'Likes': 19, 'Comments': 3}]
total_stats = {}
total_photos = 0
total_comments = 0
total_likes = 0
total_shares = 0 

for i in blog_posts:
    for key, value in i.items():
        if key == 'Photos':
            total_photos += value
        elif key == 'Likes':
            total_likes += value
        elif key == 'Comments':
            total_comments +=value
        else:
            total_shares += value

total_stats['Photos'] = total_photos
total_stats['Comments'] = total_comments
total_stats['Likes'] = total_likes
total_stats['Shares'] = total_shares
print(total_stats) 
