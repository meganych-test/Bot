mergeInto(LibraryManager.library, {
  TryVibrate: function(duration) {
    if ("vibrate" in navigator) {
      navigator.vibrate(duration);
      console.log("Vibration requested for " + duration + " milliseconds");
    } else {
      console.log("Vibration not supported in this browser");
    }
  }
});
