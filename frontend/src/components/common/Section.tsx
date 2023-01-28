import styled from "styled-components";
import { COLORS } from "./Colors";

const Section = styled.div`
    margin-top: 1em;
    padding: 1em;
    min-height: 200px;
    border-radius: 1px;
    background: ${COLORS.dark};
    box-shadow: 1px 1px 5px #000;
`;

export default Section;
