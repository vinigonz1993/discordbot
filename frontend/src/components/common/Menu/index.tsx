import styled from "styled-components";
import { COLORS } from "../Colors";

const Container = styled.div`
    width: 250px;
    z-index: 9999;
    padding: 0 !important;
    background: ${COLORS.secondary};
    left: 0 !important;
    position: fixed;
    height: 100vh !important;
    border-right: 6px solid ${COLORS.border};
`;

const UpperText = styled.h2`
    padding-top: 1em;
    padding-bottom: 1em;
    background: ${COLORS.dark};
    border-bottom: 6px solid ${COLORS.border};
`;

const Menu = () => (
    <Container>
        <UpperText>ToolBoxAPIs</UpperText>
        <ul>
            <li>OCTranspo API</li>
            <li>ChatGPT API</li>
            <li>Currency API</li>
            <li>Quotes API</li>
        </ul>
    </Container>
)

export default Menu;
