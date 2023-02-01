import React from "react";
import { Row, Col } from "react-bootstrap";
import styled from "styled-components";
import Section from "./common/Section";
import Title from "./common/Title";
import OCT from "./OCT";

const Main = () => {
    return (
        <>
            <Title title="ToolBoxAPIs"/>
            <Row>
                <Col xl={6} lg={12} md={12} sm={12}>
                    <Section>
                        OCTranstpo
                        <hr/>
                        <OCT />
                    </Section>
                </Col>
                <Col xl={6} lg={6} md={6} sm={12}>
                    <Section>
                        ChatGPT
                        <hr />
                        Coming soon
                    </Section>
                </Col>
                <Col xl={6} lg={6} md={6} sm={12}>
                    <Section>
                        Currencies
                        <hr />
                        Coming soon
                    </Section>
                </Col>
                <Col xl={6} lg={6} md={6} sm={12}>
                    <Section>
                        Quotes
                        <hr />
                        Coming soon
                    </Section>
                </Col>
            </Row>
        </>
    );
};

export default Main;
