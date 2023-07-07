import { Box, Flex, Text, Spacer} from "@chakra-ui/react";
import { Link } from "react-router-dom";

function Navbar() {
  return (
      <Flex
        as="nav"
        align="center"
        justify="space-between"
        padding="1rem"
        bg="gray.800"
        color="white"
      >
        <Box>
          <Text fontWeight="bold">Logo</Text>
        </Box>
        <Spacer />
        <Flex gap={5}>
          <Link to="/" marginRight="1rem">
            Home
          </Link>
          <Link marginRight="1rem" to="/user">User</Link>
          <Link marginRight="1rem" to="/admin">Admin</Link>
        </Flex>
      </Flex>
  );
}

export default Navbar;
