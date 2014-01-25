from django.shortcuts import render
from django.http import Http404
from tweets.models import Tweet
import tweepy,json

def index(request):
    try:
        tweet_list = Tweet.objects.all
    except Tweet.DoesNotExist:
        raise Http404
    return render(request, 'tweets/index.html', {'tweet_list': tweet_list})

def scrapper(request):
	consumer_key="36UBmR5MKNhfdOYlYHYdA"
	consumer_secret="bzvGib4mEpemMLHjgNUNwxFYikK6IECr7oufScNZ7g"
	access_token="127869815-d6EWusWl2rTwZtb78CEEk8xvOiyn2sLhRh0p8YfS"
	access_token_secret="ebJaRWFWILwTtSfB34BH9P2dNXAAIUkXKngvnwPRxE"
	auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
	auth.set_access_token(access_token, access_token_secret)
	try:
		api = tweepy.API(auth)
	except api.DoesNotExist:
		raise Http404
	name=api.me().name
	tweets = api.search(q="#nrf14",	count="2500")
	for tweet in tweets:
		if tweet.in_reply_to_status_id_str:
			reply_status=True
		else:
			reply_status=False
		if tweet.retweet_count==0:
			retweet_status=False
		else:
			retweet_status=True
		t=Tweet(text=tweet.text,time=tweet.created_at,retweet=retweet_status,reply=reply_status)
		t.save()
	return render(request, 'tweets/scrapper.html', {'name': name})


def piechart(request):
	analytics={}
	analytics['reply']=Tweet.objects.filter(reply=True).count()
	analytics['retweet']=Tweet.objects.filter(retweet=True).count()
	analytics['original']=Tweet.objects.filter(reply=False).filter(retweet=False).count()	
	result=json.dumps([{'label': k, 'value': v} for k,v in analytics.items()], indent=4)
	return render(request, 'tweets/piechart.html', {'result': result})

def linechart(request):
	slot={}
	for i in range(0,24):
		slot[i]=0
	tweets=Tweet.objects.all()
	for tweet in tweets:
		slot[tweet.time.hour]+=1
	result=json.dumps([{'label': k, 'value': v} for k,v in slot.items()], indent=4)
	return render(request, 'tweets/linechart.html', {'result': result})




















