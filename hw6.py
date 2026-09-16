blog_views = [150,800,2500,600,1200,450,3000]
trending_count = 0
for views in blog_views:
    if views > 10000:
        print("trending")
        trending_count += 1
    elif 500 <= views <= 1000:
        print("avarage")
    else:
        print("low traffic")
        
        print("total views:", sum (blog_views))
        print("trending posts:", trending_count)
        
        