import React, { useState, useEffect } from 'react';

import WordCloud from 'react-d3-cloud';

import _ from 'lodash';

import './App.css';

function App(props) {
  const [subreddits, setSubreddits] = useState({});

  // When the component is first loaded, fetch subreddits
  useEffect(fetchSubreddits, []);

  async function fetchSubreddits() {
    // Fetch all subreddits
    const response = await fetch(`/subreddits`);
    // Check if request was successful (response has 200-299 status code)
    if (response.ok) {
      const json = await response.json();
      // Response JSON has format: { 'uwaterloo': { ... }, 'UofT': { ... }, ... }
      setSubreddits(json);
    }
  }

  async function fetchWordCounts(subredditId) {
    const response = await fetch(`/subreddit/${subredditId}/topWords`);
    // Check if request was successful (response has 200-299 status code)
    if (response.ok) {
      const json = await response.json();
      // Response JSON has format: { 'wordCounts': [['midterm', 76], ['goose', 34], ...] }
      const subreddit = {
        ...subreddits[subredditId],
        wordCounts: json['wordCounts']
      };
      // Update subreddits with word count
      setSubreddits({ ...subreddits, [subredditId]: subreddit });
    }
  }

  return (
    <div className="App">
      <h1 className="App-title">CanadaU</h1>
      {_.map(subreddits, (subreddit, subreddit_id) => (
        <Subreddit
          key={subreddit_id}
          displayName={subreddit.displayName}
          subscribers={subreddit.subscribers}
          icon={subreddit.icon}
          wordCounts={subreddit.wordCounts}
          fetchWordCounts={() => fetchWordCounts(subreddit_id)}
        />
      ))}
    </div>
  );
}

function Subreddit(props) {
  const fontSizeMapper = word => word.value * 2;

  return (
    <div className="Subreddit">
      <img className="Subreddit-icon" src={props.icon} />
      <div className="Subreddit-summary">
        <h1>{props.displayName}</h1>
        <p>Subscribers: {props.subscribers}</p>
      </div>
      {!props.wordCounts && (
        <button onClick={props.fetchWordCounts}>Load Word Counts</button>
      )}
      {props.wordCounts && (
        <WordCloud
          data={props.wordCounts}
          fontSizeMapper={fontSizeMapper}
          width={300}
          height={300}
        />
      )}
    </div>
  );
}

export default App;
