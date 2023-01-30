import React, { useEffect, useState } from "react";
import { Row, Col } from "react-bootstrap";
import Input from "./common/Input";
import Section from "./common/Section";
import OCT from "./OCT";

const Main = () => {
    return (
        <>
            <h6>ToolBoxAPIs</h6>
            <hr />
            <Row>
                <Col xl={6} lg={6} md={6} sm={12}>
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
