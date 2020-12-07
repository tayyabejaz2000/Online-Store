import React, { useState } from "react";
import { BrowserRouter as Router, Switch, Route } from "react-router-dom";
import { ThemeProvider } from "@material-ui/core/styles";
import CssBaseline from "@material-ui/core/CssBaseline";
//Components
import Header from "./Components/Header";
import Footer from "./Components/Footer";

//Routes
import Home from "./Views/Home";

//Themes
import DarkTheme from "./Themes/darkTheme";
import LightTheme from "./Themes/lightTheme";

import Login from "./Components/Login";

//Vendor Components
import VendorOptions from "./Components/Vendor/VendorOptions";

function App() {
  const [dark_theme, changeThemePreference] = useState(true);
//  let theme = dark_theme ? DarkTheme : LightTheme;
let theme = LightTheme ? LightTheme : DarkTheme;

  function getTheme() {
    return [dark_theme, changeThemePreference];
  }

  return (
    <ThemeProvider theme={theme}>
      <CssBaseline />
      <Router>
        <Header themeState={getTheme} />
        <Switch>
          <Route exact path="/">
      <Login/>  
			<VendorOptions/ >

          </Route>
        </Switch>
        <Footer />
      </Router>
    </ThemeProvider>
  );
}

export default App;
