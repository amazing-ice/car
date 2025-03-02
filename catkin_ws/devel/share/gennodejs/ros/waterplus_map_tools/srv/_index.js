
"use strict";

let GetWaypointByIndex = require('./GetWaypointByIndex.js')
let GetWaypointByName = require('./GetWaypointByName.js')
let AddNewWaypoint = require('./AddNewWaypoint.js')
let SaveWaypoints = require('./SaveWaypoints.js')
let GetNumOfWaypoints = require('./GetNumOfWaypoints.js')
let GetChargerByName = require('./GetChargerByName.js')

module.exports = {
  GetWaypointByIndex: GetWaypointByIndex,
  GetWaypointByName: GetWaypointByName,
  AddNewWaypoint: AddNewWaypoint,
  SaveWaypoints: SaveWaypoints,
  GetNumOfWaypoints: GetNumOfWaypoints,
  GetChargerByName: GetChargerByName,
};
