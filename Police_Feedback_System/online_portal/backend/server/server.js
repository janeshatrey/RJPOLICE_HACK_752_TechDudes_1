// online_portal/backend/server/server.js
const express = require('express');
const bodyParser = require('body-parser');
const app = express();
const port = 3001;

app.use(bodyParser.json());

// Add your routes and controllers here

app.listen(port, () => {
  console.log(`Server is running on port ${port}`);
});
