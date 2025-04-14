import React, { useEffect, useState } from 'react';

const Leaderboard = () => {
  const [leaders, setLeaders] = useState([]);

  useEffect(() => {
    fetch('https://jubilant-winner-6994q75jr5q9fr776-8000.app.github.dev/api/leaderboard/')
      .then(response => response.json())
      .then(data => setLeaders(data))
      .catch(error => console.error('Error fetching leaderboard:', error));
  }, []);

  return (
    <div className="card">
      <div className="card-body">
        <h1 className="card-title">Leaderboard</h1>
        <table className="table table-striped">
          <thead>
            <tr>
              <th>ID</th>
              <th>Name</th>
              <th>Score</th>
            </tr>
          </thead>
          <tbody>
            {leaders.map(leader => (
              <tr key={leader._id}>
                <td>{leader._id}</td>
                <td>{leader.user?.username || 'N/A'}</td>
                <td>{leader.score}</td>
              </tr>
            ))}
          </tbody>
        </table>
      </div>
    </div>
  );
};

export default Leaderboard;
