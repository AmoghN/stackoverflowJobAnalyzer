import feedparser
import requests

def getResultSOF(searchTerm):
    # get RSS feed from StackOverFlow
    searchUrls = 'http://stackoverflow.com/jobs/feed?q={}&l={}'.format(searchTerm, "")
    # get xml text
    searchUrlHtml = requests.get(searchUrls).text

    rssFeedSOF = feedparser.parse(searchUrlHtml)
    # total results
    totalResults = rssFeedSOF.feed.os_totalresults
    # all job entries
    getJobEntries = rssFeedSOF.entries
    # job entries object
    jobResults = []
    # result object
    result = {}

    for jobEntry in getJobEntries:
        jobResult = {}
        # find employer
        if(jobEntry.get("author")):
            jobResult["employer"] = jobEntry.author
        else:
            jobResult["employer"] = None
        # find location
        if(jobEntry.get("location")):
            jobResult["location"] = jobEntry.location
        else:
            jobResult["location"] = None
        # get all job skills
        if(jobEntry.get("tags")):
            skills = []
            for skill in jobEntry["tags"]:
                skills.append(skill.term)
            jobResult["skillTags"] = skills
        else:
            jobResult["skillTags"] = None
        # allows remote
        if(jobEntry.get("title") and "allows remote" in jobEntry.get("title")):
            jobResult["remote"] = True
        else:
            jobResult["remote"] = None

        jobResults.append(jobResult)

    result["jobResults"] = jobResults
    result["totalResults"] = int(totalResults)
    return result

def getResults(searchTerm):
    sofResponse = getResultSOF(searchTerm)
    topLocations = {}
    topLangs = {}
    topEmployers = {}
    totalLangs = 0
    totalLocations = 0
    totalEmployer = 0
    totalRemote = 0

    # get all stat info
    for job in sofResponse["jobResults"]:
        # get all employer
        employer = job.get("employer")
        if(employer):
            totalEmployer += 1
            if (employer in topEmployers):
                topEmployers[employer] += 1
            else:
                topEmployers[employer] = 1

        # get all locations
        location = job.get("location")
        if(location):
            totalLocations += 1
            if (location in topLocations):
                topLocations[location] += 1
            else:
                topLocations[location] = 1

        # get all languages
        skillTags = job.get("skillTags")
        if(skillTags):
            for lang in skillTags:
                if (searchTerm.lower() not in lang):
                    totalLangs += 1
                    if (lang in topLangs):
                        topLangs[lang] += 1
                    else:
                        topLangs[lang] = 1

        # get the number of remote jobs
        if(job.get("remote")):
            totalRemote += 1

    # change to percent
    for lang in topLangs:
        topLangs[lang] = float(round(topLangs[lang]/totalLangs * 100,2))
    for location in topLocations:
        topLocations[location] = float(round(topLocations[location]/totalLocations * 100,2))
    for employer in topEmployers:
        topEmployers[employer] = float(round(topEmployers[employer]/totalEmployer * 100,2))

    # sort top results
    topLangs = sorted(topLangs.items(), key=lambda t: t[1], reverse = True)
    topLocations = sorted(topLocations.items(), key=lambda t: t[1], reverse = True)
    topEmployers = sorted(topEmployers.items(), key=lambda t: t[1], reverse = True)

    # making result object
    result = {}
    if (len(topLangs) > 10):
      result["topLangs"] = topLangs[:10]
    else:
        result["topLangs"] = topLangs
    if (len(topLocations) > 10):
        result["topLocations"] = topLocations[:10]
    else:
        result["topLocations"] = topLocations
    if (len(topEmployers) > 10):
        result["topEmployers"] = topEmployers[:10]
    else:
        result["topEmployers"] = topEmployers

    if (sofResponse["totalResults"] > 0):
        result["totalResults"] = sofResponse["totalResults"]
        result["success"] = True
    else:
         result["success"] = False

    result["totalRemote"] = totalRemote

    return result
