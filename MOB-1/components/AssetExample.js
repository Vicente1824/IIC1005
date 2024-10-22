import { Text, View, StyleSheet, Image } from 'react-native';

export default function AssetExample() {
  return (
    <View style={styles.container}>
      <Image style={styles.logo} source={require('../assets/capybara.jpeg')} />
      <Text style={styles.paragraph}>
        Soy un Capybara que vive en Argentina.
      </Text>
    </View>
  );
}

const styles = StyleSheet.create({
  container: {
    alignItems: 'center',
    justifyContent: 'center',
    padding: 24,
  },
  paragraph: {
    margin: 24,
    marginTop: 0,
    fontSize: 14,
    textAlign: 'center',
  },
  logo: {
    height: 128,
    width: 128,
  }
});
