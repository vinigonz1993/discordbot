import styled from "styled-components";
import { COLORS } from "../Colors";

const Menu = styled.div`
    width: 250px;
    z-index: 9999;
    padding: 0 !important;
    background: ${COLORS.secondary};
    left: 0 !important;
    position: fixed;
    height: 100vh !important;
`;

export default Menu;
