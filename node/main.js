const rp = require('request-promise');
const $ = require('cheerio');

const url = 'http://www.jobs.com/jobs/search?q=operation+research+analyst&where=&lat=&lon=&gt=';

var headers = { 
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64; rv:44.0) Gecko/20100101 Firefox/44.0',
    'Content-Type' : 'application/x-www-form-urlencoded' 
};

options = {
    uri: url,
    headers: headers,
    json: true
}
rp(options)
  .then(function(html){
    //success!
    //console.log(html);
    console.log($('.review').text());
  })
  .catch(function(err){
    //handle error
    console.log('fail');
  });
  