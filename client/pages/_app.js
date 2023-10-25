// Import the Bootstrap CSS to apply styling to your components.
import 'bootstrap/dist/css/bootstrap.css';

// Import the 'buildClient' function from the '../api/build-client' module.
import buildClient from '../api/build-client';

// Import the 'Header' component from the '../components/header' module.
import Header from '../components/header';

// Define the 'AppComponent' functional component that receives 'Component', 'pageProps', and 'currentUser' as props.
const AppComponent = ({ Component, pageProps, currentUser }) => {
  return (
    <div>
      {/* Render the 'Header' component with 'currentUser' as a prop. */}
      <Header currentUser={currentUser} />

      {/* Render the 'Component' with 'pageProps'. */}
      <Component {...pageProps} />
    </div>
  );
};

// Define the 'getInitialProps' function on the 'AppComponent'.
AppComponent.getInitialProps = async appContext => {
  // Create a client using the 'buildClient' function, passing the context ('appContext.ctx').
  const client = buildClient(appContext.ctx);

  // Send a request to '/api/users/currentuser' to fetch user data and store it in the 'data' variable.
  const { data } = await client.get('/api/users/currentuser');

  // Initialize 'pageProps' as an empty object.
  let pageProps = {};

  // Check if 'appContext.Component.getInitialProps' exists and if it does, invoke it.
  if (appContext.Component.getInitialProps) {
    pageProps = await appContext.Component.getInitialProps(appContext.ctx);
  }

  // Return an object containing 'pageProps' and 'data' to be passed as props.
  return {
    pageProps,
    ...data
  };
};

// Export the 'AppComponent' as the default export of this module.
export default AppComponent;
