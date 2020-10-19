SearchFunction
/**
 * The searching function.
 * @callback callback function which is called after the tweet is returned.
 */
function search(callback) {
/**
   * Gets a search key from data.js.
   * @private
   */
  function getSearchKey() {
    let searchKeys = require('./data.js').searchKeys;
    return searchKeys[Math.floor(Math.random() * searchKeys.length)].toLowerCase();
  }
Twitter.get(
    'search/tweets',
    { q: getSearchKey(), count: 50, lang: 'en' },
    function(err, data, response) {
      let tweetList = [];
      if (!err) {
        for (let i = 0; i < data.statuses.length; i++) {
          let tweet = data.statuses[i];
          tweetList.push(tweet);
        }
        callback(tweetList);
        return;
      } else {
        console.log(err);
      }
    }
  );
}
function main(){
	search("Fact check this")
}