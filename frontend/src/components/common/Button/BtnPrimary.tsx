import { Button } from "react-bootstrap";
import styled from "styled-components";
import { COLORS } from "../Colors";

const BtnPrimary = styled(Button)`
    background: ${COLORS.primary};
    border: 1px solid ${COLORS.border};
    border-radius: 1px;
    padding: 3px;
    width: 100%;
    padding-left: 6px;
    padding-right: 6px;
    font-size: 0.65em;
    color: #ffffff;

    &:hover {
        background: ${COLORS.dark};
        border: 1px solid ${COLORS.primary};
        color: #fff;
        font-weight: bold;
    }
`;

export default BtnPrimary;